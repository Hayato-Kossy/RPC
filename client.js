// client.jsの内容
const net = require('net');
const HOST = 'localhost';
const PORT = 12345;

let client = new net.Socket();

// リクエストの作成
let request = {
    "method": "reverse",
    "params": ["ちんちん"],
    "param_types": ["float"],
    "id": 1
}

client.connect(PORT, HOST, function() {
    console.log('Connected to: ' + HOST + ':' + PORT);

    // リクエストの送信
    client.write(JSON.stringify(request));
});

client.on('data', function(data) {
    // レスポンスの受信と解析
    let response = JSON.parse(data);
    console.log('Received: ', response);

    client.destroy();
});

client.on('close', function() {
    console.log('Connection closed');
});
