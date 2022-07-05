# Exception Handling
### There are two types of errors in Python

1. Syntax Errors
2. Runtime Errors

### Syntax Errors
Exp:
imprt sys 
#>>> SyntaxError 

Note: For Syntax Error there is not handling, you need to input standard input for programm to recognize

### Runtime Errors
The synatax might be correct but you can get an error.
<br> Exp: 
<br> >>> import boto3 
<br> ModuleNotFoundError: No module named 'boto3'

To handle the Runtime Errors you need to implement ####  <b>Try</b> and <b>excpet</b> block

```
dir(boto3)   will show you all available operations under boto3

dir(boto3.exceptions) will show you the available exceptions under exceptions 
```

### You can find exception in botocore as well by executing
```
dir(boto3.exceptions.botocore.exceptions)
```
boto3 is built on top of botocore and you can find all available exceptions over there as well 

### By default when you install boto3 the botocore is also available with your host