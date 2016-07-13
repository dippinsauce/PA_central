# PA_central

Build a REST API on flask for data collection and controlling action.

    database: "home"
        table: "server_status"
            column: "id" INT NOT NULL PRIMARY KEY AUTO_INCREMENT
            column: "temp" FLOAT
            column: "load_avg" FLOAT

    database: "lake"
	    table: "interior_temp"
		    column: "id" INT NOT NULL PRIMARY KEY AUTO_INCREMENT
		    column: "timestamp" TIMESTAMP
		    column: "temp" FLOAT
		    column: "humidity" FLOAT
	    table: "test"
		    column: "id" INT NOT NULL PRIMARY KEY AUTO_INCREMENT
		    column: "timestamp" TIMESTAMP
		    column: "test_float" FLOAT
		    column: "test_int" INT


