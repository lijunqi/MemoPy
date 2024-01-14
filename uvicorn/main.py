async def app(scope, receive, send):
    # 一个最简单的ASGI应用程序
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })


if __name__ == "__main__":
    # uvicorn服务
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
