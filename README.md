# aws-sam-cli-helloworld

## Vagrant setup
### setup
```
## 初回のみ
$ vagrant box add centos72 https://github.com/CommanderK5/packer-centos-template/releases/download/0.7.2/vagrant-centos-7.2.box

$ cd /path/to/aws-sam-cli-helloworld/centos72
$ vagrant up
$ vagrant ssh
```

## DynamoDB
```
$ cd ~/dynamo
$ java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```

https://github.com/aaronshaf/dynamodb-admin

GUIで操作できるツールを利用します。

以下で起動するとアクセス可能となります。
```
export DYNAMO_ENDPOINT=http://localhost:8000
dynamodb-admin
```


## sam
```
$ ~/dev/sam-app
$ pip install -r requirements.txt -t hello_world/build/
$ cp hello_world/*.py hello_world/build/
$ sam local generate-event apigateway aws-proxy > event_file.json
$ sam local start-api
```

curl等でアクセスすることでAPIを呼び出せます。

また、Vagrantで立ち上げたにアクセスるる際は以下にてアクセス可能です(/etc/httpd/conf.d/local.confで設定されています)。

```
$ curl http://[VMのIPアドレス]:89/hello?username=hogeuser
```
