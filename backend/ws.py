from fastapi import FASTAPI, WebSocket, WebSocketDisconnect

app = FASTAPI()

connections=[]

@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    connections.append(websocket)

    try: 
        while True:
            data = await websocket.receive_text()
            for conn in connections:
                await conn.send_text(f"Someone said:{data}")
    except WebSocketDisconnect:
        connections.remove(websocket)