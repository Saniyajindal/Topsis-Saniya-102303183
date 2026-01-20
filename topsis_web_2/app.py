<!DOCTYPE html>
<html>
<head>
    <title>TOPSIS Analysis Web Tool</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f6f9;
        }
        .box {
            width: 450px;
            margin: 60px auto;
            padding: 25px;
            background: white;
            border-radius: 10px;
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
        }
        button {
            background: green;
            color: white;
            font-size: 16px;
            border: none;
        }
    </style>
</head>
<body>

<div class="box">
    <h2>TOPSIS Analysis</h2>

    <form method="post" enctype="multipart/form-data">
        <label>Upload File (.csv / .xlsx)</label>
        <input type="file" name="file" required>

        <label>Weights (comma separated)</label>
        <input type="text" name="weights" placeholder="1,2,1,1" required>

        <label>Impacts (+ or -)</label>
        <input type="text" name="impacts" placeholder="+,+,-,+" required>

        <button type="submit">Run TOPSIS Analysis</button>
    </form>
</div>

</body>
</html>
