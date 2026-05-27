<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <title>સિલેક્શન બેઝ્ડ પ્રશ્ન બેંક</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; }
        .container { max-width: 800px; margin: auto; }
        select, button { padding: 10px; margin: 5px; width: 90%; }
        button { background-color: #2196F3; color: white; border: none; cursor: pointer; }
        #output { margin-top: 20px; border-top: 2px solid #333; padding-top: 10px; }
    </style>
</head>
<body>

<div class="container">
    <h1>પ્રશ્ન બેંક પસંદગીકાર</h1>
    
    <label>ધોરણ અને વિષય પસંદ કરો:</label>
    <input type="text" id="subName" placeholder="દા.ત. ધોરણ 10 વિજ્ઞાન" style="width: 87%; padding: 10px; margin: 5px;">

    <label>પાઠ પસંદ કરો:</label>
    <select id="chapterSelect">
        <option value="પાઠ 1">પાઠ 1</option>
        <option value="પાઠ 2">પાઠ 2</option>
        <option value="પાઠ 3">પાઠ 3</option>
        <option value="પાઠ 4">પાઠ 4</option>
        <option value="પાઠ 5">પાઠ 5</option>
    </select>

    <button onclick="generate()">પ્રશ્નો જુઓ</button>

    <div id="output"></div>
</div>

<script>
    function generate() {
        const sub = document.getElementById('subName').value;
        const chap = document.getElementById('chapterSelect').value;
        const output = document.getElementById('output');

        if(sub === "") { alert("વિષયનું નામ લખો!"); return; }

        let html = `<h2>${sub} - ${chap}</h2>`;
        for(let i = 1; i <= 100; i++) {
            html += `<p><strong>પ્રશ્ન ${i}:</strong> ${chap} નો મહત્વનો પ્રશ્ન ${i} અહીં પ્રદર્શિત થશે.</p>`;
        }
        output.innerHTML = html;
    }
</script>

</body>
</html>
