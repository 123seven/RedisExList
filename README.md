
```
 _____    _____   _____   _   _____   _____  __    __  _       _   _____   _____  
|  _  \  | ____| |  _  \ | | /  ___/ | ____| \ \  / / | |     | | /  ___/ |_   _| 
| |_| |  | |__   | | | | | | | |___  | |__    \ \/ /  | |     | | | |___    | |   
|  _  /  |  __|  | | | | | | \___  \ |  __|    }  {   | |     | | \___  \   | |   
| | \ \  | |___  | |_| | | |  ___| | | |___   / /\ \  | |___  | |  ___| |   | |   
|_|  \_\ |_____| |_____/ |_| /_____/ |_____| /_/  \_\ |_____| |_| /_____/   |_|                                                                                    
                                                                                                                                                                                   
```

![](https://img.shields.io/badge/language-python-orange.svg)
![](https://img.shields.io/cocoapods/l/Alamofire.svg?style=flat)  

Python Redis 过期列表。项目中用于管理微信小程序的[formId](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/template-message.html)

## 使用示例

```python
    import RedisExList
    ex_list = RedisExList(expiration=60)
    ex_list.set_value('key', 'value')
    ex_list.get_value('key')
```


## License

This work is released under the MIT license. A copy of the license is provided in the [LICENSE](./LICENSE) file.

