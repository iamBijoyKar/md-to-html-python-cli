

TAGSH = {
    1 : "<h1> $tag$ </h1>",
    2 : "<h2> $tag$ </h2>",
    3 : "<h3> $tag$ </h3>",
    4 : "<h4> $tag$ </h4>",
    5 : "<h5> $tag$ </h5>",
}

CONFIG_BOILER = {
    "rootDir": "",
    "outDir": "",
}

CONFIG_FILE_NAME = 'bkar.congif.json'

BKAR_BOILER = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title$</title>
</head>
<body>
    $body$
</body>
</html>
"""