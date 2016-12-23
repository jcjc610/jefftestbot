# CONSTANTS LIST:

###BOT DETAILS###
# ENTER YOUR BOT API TOKEN FROM @BOTFATHER HERE:
BOT_TOKEN = ""
# ENTER YOUR BOT'S USERNAME WITHOUT '@' 
BOT_USERNAME = ""

###ADMIN DETAILS###
# ENTER YOUR NAME:
ADMIN_NAME = ""
# ENTER YOUR TELEGRAM ID:
ADMIN_ID = 123456789
# ENTER YOUR TIME ZONE (TZ FORMAT, EXAMPLE: 'ASIA/HONG_KONG')
ADMIN_TIMEZONE = ""

###MYSQL DETAILS###
# ENTER YOUR SERVER NAME
MYSQL_SERVER = "localhost"
# ENTER YOUR MYSQL USERNAME
MYSQL_USERNAME = ""
# ENTER YOUR MYSQL PASSWORD
MYSQL_PW = ""
# ENTER YOUR MYSQL DATABASE NAME
MYSQL_DBNAME = ""

###ACCUWEATHER API DETAILS###
# ENTER YOUR ACCUWEATHER API KEY (AT THE MOMENT USING 2 API KEYS)
# OPTAINED AT DEVELOPER.ACCUWEATHER.COM
ACCU_API_1 = ""
ACCU_API_2 = ""

### CREATE TABLE SQL, DO NOT AMEND###
SQL_CREATE_TABLE_1 = "CREATE TABLE IF NOT EXISTS `feedback` (`id` int(11) NOT NULL AUTO_INCREMENT, `message` mediumtext NOT NULL, `name` varchar(200) NOT NULL, `username` varchar(100) NOT NULL, `telegramid` int(20) NOT NULL, PRIMARY KEY (`id`), UNIQUE KEY `id` (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4"
SQL_CREATE_TABLE_2 = "CREATE TABLE IF NOT EXISTS `group` (`id` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(150) NOT NULL, `groupid` bigint(30) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4"
SQL_CREATE_TABLE_3 = "CREATE TABLE IF NOT EXISTS `patdb` (`patid` int(11) NOT NULL AUTO_INCREMENT, `patdesc` text NOT NULL, PRIMARY KEY (`patid`), UNIQUE (`patid`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4"
SQL_CREATE_TABLE_4 = "CREATE TABLE IF NOT EXISTS `user` (`userid` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(100) NOT NULL, `username` varchar(100) NOT NULL, `telegramid` int(20) NOT NULL, `patted` int(11) NOT NULL, `pattedby` int(11) NOT NULL, `loc` varchar(50) DEFAULT NULL, PRIMARY KEY (`userid`), UNIQUE KEY `userid` (`userid`, `telegramid`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4"
SQL_DEFAULT_PAT = "INSERT INTO `patdb` (`patid`, `patdesc`) VALUES (1, 'is patted by'), (2, 'is again patted by')"
