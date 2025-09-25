from sqlalchemy.orm import Session

def create_session_with_users(db: Session, session_data, user_ids):
    try:
        # Create a new SessionModel object using the provided session_data dictionary
        # Example: {"name": "Team Chat"} → SessionModel(name="Team Chat")
        session = SessionModel(**session_data)

        # Stage the new session object for insertion into the database
        # (nothing is actually written to the DB yet)
        db.add(session)

        # Push pending changes to the DB so that auto-generated fields (like session.id)
        # are available, but without committing the transaction
        db.flush()

        # Loop through the list of user IDs to create participant entries
        for uid in user_ids:
            # Create a new Participant object linking each user to this session
            participant = Participant(session_id=session.id, user_id=uid)

            # Stage the participant object for insertion (still not yet written to DB)
            db.add(participant)

        # Commit the transaction → all INSERTs for session and participants
        # are executed together. If this succeeds, changes are permanent.
        db.commit()

        # Refresh the session object to load the latest data from the DB
        # (useful for auto-generated fields like id, created_at, etc.)
        db.refresh(session)

        # Return the fully created session object (with its ID and other fields populated)
        return session

    except:
        # If ANY error occurs, undo all staged/committed operations in this transaction
        # This prevents partial data from being saved
        db.rollback()

        # Re-raise the error so the caller knows something went wrong
        raise
