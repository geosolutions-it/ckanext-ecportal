ckanext-ecportal
================

EC PORTAL
---------

Porting [ckanext-ecportal](https://github.com/okfn/ckanext-ecportal) extension to version 2.x


Install
-------


```
   . /usr/lib/ckan/default/bin/activate
   git clone https://github.com/geosolutions-it/ckanext-ecportal.git 
   cd /usr/lib/ckan/default/src/ckanext-ecportal
   python setup.py develop
```

Edit yout ``.ini`` file and add ``ecportal`` to the plugin line:
```
   ckan.plugins = [...other plugins...] ecportal
```
