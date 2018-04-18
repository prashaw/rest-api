
## Rest API Instructions
To run this program, you should download this program to local. If you have not yet install flask, you can install flask from http://flask.pocoo.org. In the terminal, you can type in ```FLASK_APP=restaurant_api.py flask run``` to run the program
For any problems you can contact me at prw19 at pitt dot edu

### GET
```
GET /restaurant/:restaurant_name
```
This get command will return restaurant that matches the given restaurant name. If the restaurant does not exist, it will return "Restaurant successfully added" with status code of 404. Upon successful command, it will return the restaurant information in a json format.

```
GET /menuitem/:menuitem_name
```
This get command will return all the menuitems that are identical to the given menuitem name. If the menuitem does not exist, it will return "None is found" with status code of 404. Upon successful command, all menuitems that matches the name will be returned in json format.

### POST
```
POST /restaurant/:restaurant_name
```
This post command will add the restaurant to our current database. If the restaurant is not in the database and is successfully added, It will return "Restaurant successfully added" and status code of 201. If the restaurant is already in our database, it will return "Restaurant already exists in database"

```
POST /menuitem/:restaurant_name/:menu_name/:menuitem_name
```
This post command for menuitem will add the menuitem to the given restaurant and menu. If the given restaurant_name is not in database, it will return "Restaurant does not exist in database" with status code of 404. If the menuitem is successfully added, it will return "Menuitem for restaurant successfully added"

### DELETE
```
DELETE /restaurant/:restaurant_name
```
This delete command will delete the restaurant with the give name. If the restaurant is not in the database, it will return "Restaurant not in database" with status code of 404. Else if the restaurant is successfully deleted, it will return "Restaurant deleted successfully"

```
DELETE /menuitem/restaurant_name/menu_name/menuitem_name
```
This delete command will delete the given menuitem given restaurant and menu. If the provided restaurant name is not in database, it will return "Restaurant does not exist" with status code of 404. If the the restaurant does not have the dish under the restaurant and menu, it will return "The restaurant does not have this menu item" with status code of 404. Else, it will return "Menu item deleted successfully" to indicate successful deletion.

### POST
```
POST /restaurant/:old_restaurant_name/:new_restaurant_name
```
This post command will change the given old restaurant name to the new restaurant name. If old_restaurant_namedoes not exist in database, it will return "Restaurant does not exist" with status code of 404. Else, it will return the new restaurant informataion in json format.
