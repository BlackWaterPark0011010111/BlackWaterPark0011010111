"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
​
    <style>
        /* This is a CSS comment */
        p {
            /* Note: text color is inherited to child elements */
            color: darkblue; /* Set the text color */
        }
​
        /*
            Another note:
            Notice the website has some "style" even without CSS
​
            The browser contains some default styling for HTML
            Different browsers can look slightly different
        */
​
        body {
            background: lightpink;
        }
​
        img {
            border: 15px double darkblue;
            border-radius: 50%;
        }
    </style>
​
</head>
<body>
    <!-- This is a HTML comment -->
​
    <!-- H1 is an element, title is an attribute -->
    <h1 title="Hello hello hello">Hello world</h1>
    <h2>Welcome to my website</h2>
    <!-- Ctrl+z to undo -->
​
    <!-- H1, H2 and P are all block elements -->
    <!-- EM and STRONG elements are inline elements -->
    <p>This is the page of <em>Joel</em>!!!</p>
    <p>Welcome, and <strong>thank you</strong>!</p>
    <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi labore maxime tempore ut esse minima deserunt ipsum sint aliquid facere harum saepe architecto, eaque porro repudiandae maiores quae eius doloremque!
    </p>
​
    <!-- This was generated with emmet "p>lorem" -->
    <p>Lorem ipsum <strong>dolor</strong> sit amet consectetur adipisicing elit. Optio commodi et doloribus voluptate dolores. Quasi hic animi optio tempore consequatur ipsam dolorem expedita consequuntur at voluptate architecto, velit minus a?</p>
​
    <hr>
​
    <img src="https://placekeanu.com/200/150" alt="Image of Keanu Reeves">
    <img src="myface.png" alt="Image of cat">
​
    <!-- Slightly more advanced Emmet thing -->
    <!-- ul>li*5>lorem5 , then changed to an Ordered list -->
    <ol>
        <li>Lorem ipsum dolor sit amet.</li>
        <li>Voluptate eius debitis hic perferendis.</li>
        <li>Molestias rem doloribus deserunt itaque.</li>
        <li>Corrupti itaque nulla a vero.</li>
        <li>Asperiores maxime minus sed et!</li>
    </ol>
​
</body>
</html>
"""