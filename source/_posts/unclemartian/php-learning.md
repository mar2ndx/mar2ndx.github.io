---
title: 【Tech】 PHP learning notes
category: unknown
tags: technology
comments: true
date: 2015-05-31 00:00:00
---


# PHP language

## web server must have a php server

web server: Apache, IIS, Tomcat, JBoss, WebLogic...

app server: Jsp, PHP, Asp...

we also need database, but does need to be at same machine as web/app server.

## A Comparison

Linux   +  Apache  + MySql      +  PHP  =  LAMP      - open sourced, dev speed fastest

Unix    +  Tomcat  + Oracle     +  JSP  =  J2EE      - most expensive

Windows +  IIS     + SQL server +  ASP  =  ASP.net   - virus risks, very not safe

## To get information from POST form

        Hi <?php echo htmlspecialchars($_POST['name']); ?>.
        You are <?php echo (int)$_POST['age']; ?> years old.

## Superglobals

build-in variables that are always available in all scopes. like:

1. $GLOBALS, variables available in global scope

        <?php
        function test() {
            $foo = "local variable";
            echo '$foo in global scope: ' . $GLOBALS["foo"] . "\n";
            echo '$foo in current scope: ' . $foo . "\n";
        }

        $foo = "Example content";
        test();
        ?>

1. $_SERVER, Server and execution environment information

        <?php
        echo $_SERVER['SERVER_NAME'];
        ?>

1. $_GET, GET variables

        <?php
        echo 'Hello ' . htmlspecialchars($_GET["name"]) . '!';
        ?>

1. $_POST, POST variables

        <?php
        echo 'Hello ' . htmlspecialchars($_POST["name"]) . '!';
        ?>

1. $_FILES, File Upload variables
1. $_COOKIE
1. $_SESSION
1. $_REQUEST

    The PHP $_REQUEST variable contains the contents of both $_GET, $_POST, and $_COOKIE.

1. $_ENV, Environment variables

    These variables are imported into PHP's global namespace from the environment under which the PHP parser is running. Many are provided by the shell under which PHP is running.

## php code to print a variable:

    <html>
            <body>
            <?php
            $capital = 67;
            print("Variable capital is $capital<br>");
            print("Variable CaPiTaL is $CaPiTaL<br>");
            ?>
            </body>
    </html>

## preg_match

in PHP does a regex match.

## include() and require()

__The include() function__ takes all the text in a specified file and copies it into the file that uses the include function.

__The require() function__ takes all the text in a specified file and copies it into the file that uses the include function. If there is any problem in loading a file then the require() function __generates a fatal error and halt the execution of the script__.

## a list of PHP - Predefined Variables

can be found here:

http://www.tutorialspoint.com/php/php_predefined_variables.htm

## define a error-handling function:

        error_function(error_level, error_messag, error_file,error_line, error_context);

# PHP OOP

## PHP Classes

        <?php
        class  Books{
            /* Member variables */
            var $price;
            var $title;
            /* Member functions */
            function setPrice($par){
               $this->price = $par;
            }
            function getPrice(){
               echo $this->price ."<br/>";
            }
            function setTitle($par){
               $this->title = $par;
            }
            function getTitle(){
               echo $this->title ." <br/>";
            }
        }
        ?>

## Creating Objects

        $physics = new Books( "Physics for High School", 10 );
        $maths = new Books;
        $chemistry = new Books;

        $physics->setTitle( "Physics for High School" );
        $maths->setTitle( "Algebra" );
        $chemistry->setTitle( "Advanced Chemistry" );

## Public and Private members

Unless you specify otherwise, properties and methods of a class are public.

If you wish to limit the accessibility of the members of a class then you define class members as private or protected.

        class MyClass {
           private $car = "skoda";
           $driver = "SRK";

           function __construct($par) {
              // Statements here run every time
              // an instance of the class
              // is created.
           }

           function myPublicFunction() {
              return("I'm visible!");
           }
           private function myPrivateFunction() {
              return("I'm  not visible outside!");
           }
        }

## Interfaces

        interface Mail {
           public function sendMail();
        }

        class Report implements Mail {
           // sendMail() Definition goes here
        }

## Constants

constant's name does not have a leading $, as variable names do.

        class MyClass {
           const requiredMargin = 1.7;
           function __construct($incomingValue) {
              // Statements here run every time
              // an instance of the class
              // is created.
           }
        }

## Abstract Classes

When inheriting from an abstract class, all methods marked abstract in the parent's class declaration must be defined by the child.

It is not legal to have abstract function definitions inside a non-abstract class.

        abstract class MyAbstractClass {
           abstract function myAbstractFunction() {
           }
        }

## Static

A member declared as static can not be accessed with an instantiated class object (though a static method can).

        <?php
        class Foo
        {
            public static $my_static = 'foo';

            public function staticValue() {
                return self::$my_static;
            }
        }
        print Foo::$my_static . "\n";
        $foo = new Foo();
        print $foo->staticValue() . "\n";

## Final Keyword

Prefixing the method definition with final prevents child classes from overriding.

If the class itself is being defined final then it cannot be extended.

## Calling parent constructors

The constructor of NameSub1 functions by calling its parent constructor explicitly using the :: syntax.

        class Name
        {
           var $_firstName;
           var $_lastName;
           function Name($first_name, $last_name)
           {
             $this->_firstName = $first_name;
             $this->_lastName = $last_name;
           }
           function toString() {
             return($this->_lastName .", " .$this->_firstName);
           }
        }
        class NameSub1 extends Name
        {
           var $_middleInitial;
           function NameSub1($first_name, $middle_initial, $last_name) {
               Name::Name($first_name, $last_name);
               $this->_middleInitial = $middle_initial;
           }
           function toString() {
               return(Name::toString() . " " . $this->_middleInitial);
           }
        }

## Reference

http://php.net/

http://www.tutorialspoint.com/php/index.htm

http://www.w3schools.com/php/
