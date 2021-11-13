# user_agent2
* Inherit from user_agent. 
* Append recently browser version.

# Usage Example
```python

from user_agent2 import (
    generate_user_agent,
)

ua = generate_user_agent(navigator="chrome")
print(ua)
```
