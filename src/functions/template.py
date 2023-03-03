

TAGSH = {
    1 : '<h1 class="$class$"> $tag$ </h1>',
    2 : '<h2 class="$class$"> $tag$ </h2>',
    3 : '<h3 class="$class$"> $tag$ </h3>',
    4 : '<h4 class="$class$"> $tag$ </h4>',
    5 : '<h5 class="$class$"> $tag$ </h5>',
    0 : '<p class="$class$"> $tag$ </p>'
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

DEFAULT_STYLE = """

    *{
        box-sizing: border-box;
        padding: 0;
    }
    html{
        font-family: sans-serif;
    }

"""