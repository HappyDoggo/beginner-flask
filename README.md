# beginner-flask

I have no idea what I'm doing.

## Powershell
[Running Flask in Powershell.](https://github.com/pallets/flask/issues/2281)
```
$env:FLASK_APP = "hello.py"
$env:FLASK_DEBUG = "1"
flask run
```
If not running in virtual environment, remove the variables after use.
```
Remove-Item Env:\FLASK_APP
Remove-Item Env:\FLASK_DEBUG
```
Check variables using `Get-ChildItem Env:`.

## To do
- [ ] get a virtual environment.
- [ ] basic random generator prototype.
