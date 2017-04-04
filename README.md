# Programming Language Interpreter
Implementation of a Simple Interpreter in Python.

Currently supports `Assignment`, `While`, `Print`, `Branch` and `Comment` Statements.

## Syntax

### Assignment Statement
Doesn't Support Parentheses.

Example
```
a = 1;
b = 11;
x = a+b;
z = a*b +z/b;
```
### Print Statement
Python3-style print statement.

Using variables from above example
```
print("Value of x is ",x," and value of z is ",z);
```


### While Statement

`while` , `do` and `done` and  are keywords.

Example
```
fact = 1;
limit = 6;

while limit>1 do
  fact = fact*limit;
  limit = limit-1;
done;
```

### Branch Statement
Supports `if` , `if...else` and `nested-if` statements.

Example
```
x=1;
y=2;
z=3;

if x<y then
	if z<y then
		ans = y;
	else
		ans = z;
	fi;
else
	if z>x then
		ans = z;
	else
		ans = x;
	fi;
fi;

print("Minimum Value is ",ans);
```

### Comment Statements
Comments Start from `<!--` and ends with `-->`.

Example
```
<!--
This is a Comment.
-->

x=1;
y=2;
z=3;

```

