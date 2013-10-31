$(function () {
    var WEB_SOCKET_SWF_LOCATION = '/_static/js/socketio/WebSocketMain.swf';
    var socket = io.connect('/test');
    socket.on('connect', function (data) {
        socket.emit('join', 'hello!');
    });
    socket.on('recive', function (data) {
        console.log(data);
        $('#lines').append("<p>" + data + "</p>");
    });
});
