# ParkApi

# Design Document

## APIs List

- admin
- get_spesific_park_areas/<pk>
- add_park_areas
- display_close_areas
- delete_areas/<pk>


## API's Details

------------
### 1. get_spesific_park_areas/{AreaId}
  
This end point return information about specific park area.
  
Request Type: GET<br>
Return Codes: 200, 204<br>
Response Type: JSON<br>

### return output example:
```json
{
    "id": 1,
    "latitude": 38.420942,
    "longitude": 27.308414,
    "comment": "Comment in here",
    "created_by": "Username"
}
```


### 2. add_park_areas

This end point create  park areas.

Request Type: POST<br>
Return Codes: 201, 400<br>
Parameters: latitude, longitude, comment, created_by<br>
Response Type: JSON<br>

### return output example:
```json
{
    "id": 1,
    "latitude": 38.420942,
    "longitude": 27.308414,
    "comment": "Comment in here",
    "created_by": "Username"
}
```

### 3. display_close_areas
This end point display close park areas using distance.

Request Type: POST<br>
Return Codes: 200, 204, 400<br>
Parameters: latitude, longitude, distance<br>
Response Type: JSON<br>

```json
[
    {
        "id": 4,
        "latitude": 38.614033,
        "longitude": 27.429562,
        "comment": "Comment in here",
        "created_by": "Username"
    },
    {
        "id": 5,
        "latitude": 38.60845,
        "longitude": 27.41834,
        "comment": "Comment in here",
        "created_by": "Username"
    },
    {
        "id": 6,
        "latitude": 38.601891,
        "longitude": 27.06781,
        "comment": "Comment in here",
        "created_by": "Username"
    },
    {
        "id": 7,
        "latitude": 38.420942,
        "longitude": 27.308414,
        "comment": "This is an information message",
        "created_by": "Username"
    }
]

```

### 4.delete_areas/{AreaId}

This end point delete parking areas.

This end point display close park areas using distance.

Request Type: POST<br>
Return Codes: 202, 204<br>
Parameters: AreaId<br>
Response Type: JSON<br>
