<html>
  <head>
    <title>Задачи на день</title>
    <link rel="stylesheet" href="css/styles.css">

    <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="js/script.js"></script>
  </head>
  <body>
  <div class="container">
    <h1>Текущие задачи</h1>
     <ul id="todo-list"></ul>
  % for task in tasks:
    <li>
      <input class='checkbox' type='checkbox' />
      {{ task.description }}
      <a class="remove" href="#">X</a>
      <hr/>
    </li>
  % end
  <br/>
     
   
  </div>
  </body>

</html>