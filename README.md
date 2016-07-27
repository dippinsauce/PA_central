# PA_central

Build a REST API on flask for data collection and controlling action.



App routing
/   serve switchboard, one look status board

    /lake
    ...

    /home
    /home/server_status
        POST = send server temperature and load average, store in database.
    /home/test
        POST = send dummy numbers and store in database == TESTING ==


Database configurations / tables

    database: "default"
        table: "home_server_status"
            column: "id" INT NOT NULL PRIMARY KEY AUTO_INCREMENT
            column: "post_time" DATETIME
            column: "temp" FLOAT
            column: "load_avg" FLOAT
	    table: "lake_interior_temp"
		    column: "id" INT NOT NULL PRIMARY KEY AUTO_INCREMENT
		    column: "post_time" DATETIME
		    column: "temp" FLOAT
		    column: "humidity" FLOAT
	    table: "test"
		    column: "id" INT NOT NULL PRIMARY KEY AUTO_INCREMENT
		    column: "post_time" DATETIME
		    column: "test1" FLOAT
		    column: "test2" INT


