

# this one authenticates with my test account

curl - v
'https://developer.api.autodesk.com/authentication/v1/authenticate' - X
'POST' - H
'Content-Type: application/x-www-form-urlencoded' - d
'client_id=0njO39Ges7ueLAbOB3eVYNsW8venF2mJ' - d
'client_secret=LPrOXsCgEgUzVHwv' - d
'grant_type=client_credentials' - d
'scope=data:read' - d
'scope=data:write'

