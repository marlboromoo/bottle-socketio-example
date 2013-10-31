# bottle-socketio-example
Example for using bottle.py with redis and socket.io.

## Requirments 
 - Python
 - [hiredis-py] []
 - [redis-py] []
 - [bottle.py] []
 - [bottle-redis] []
 - [gevent] []
 - [gevent-socketio] []

## Install

### Dependency
```sh
sudo su -
apt-get install python python-dev python-pip build-essential redis-server
pip install hiredis redis bottle bottle-redis gevent gevent-socketio
```
### Usage
 * Start the web server.

```sh
python web.py 
```

 * Open web browser to http://127.0.1.1:8080/  
 * Push the message.

```sh
for i in 1 2 3 4 5; do
    python tool/push.py
done
```

## Author
Timothy.Lee a.k.a MarlboroMoo.

## License
Released under the [MIT License].

  [MIT License]: http://opensource.org/licenses/MIT "MIT License"
  [hiredis-py]: https://github.com/redis/hiredis "hiredis-py"
  [redis-py]: https://github.com/andymccurdy/redis-py "redis-py"
  [bottle.py]: https://github.com/defnull/bottle "bottle.py"
  [bottle-redis]: https://github.com/bottlepy/bottle-extras/tree/master/redis "bottle-redis"
  [gevent]: https://github.com/surfly/gevent "gevent"
  [gevent-socketio]: https://github.com/abourget/gevent-socketio "gevent-socketio"

