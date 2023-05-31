document.addEventListener('DOMContentLoaded', function() {
    var jsonFileInput = document.getElementById('jsonFileInput');
    var generateButton = document.getElementById('generateButton');
    var copyButton = document.getElementById('copyButton');
    var outputText = document.getElementById('outputText');
    var jsonData;

    jsonFileInput.addEventListener('change', function(e) {
        var file = e.target.files[0];
        var reader = new FileReader();
        reader.onload = function(e) {
            var contents = e.target.result;
            try {
                jsonData = JSON.parse(contents);
            } catch (error) {
                console.error('Error parsing JSON file:', error);
                alert('Invalid JSON file. Please try again.');
            }
        };
        reader.readAsText(file);
    });

    generateButton.addEventListener('click', function() {
        if (jsonData && jsonData.length > 0) {
            generateButton.classList.add('btn-animation');
            setTimeout(function() {
                generateButton.classList.remove('btn-animation');
                var randomValue = getRandomValue(jsonData);
                outputText.value = getRandomValueText(randomValue);
                resizeTextarea();
            }, 500);
        } else {
            alert('Please upload a valid JSON file first.');
        }
    });

    copyButton.addEventListener('click', function() {
        copyButton.classList.add('btn-animation');
        setTimeout(function() {
            copyButton.classList.remove('btn-animation');
        }, 500);
        outputText.select();
        document.execCommand('copy');
    });

    function getRandomValue(data) {
        var randomIndex = Math.floor(Math.random() * data.length);
        var randomValue = {};
        var item = data[randomIndex];
        for (var key in item) {
            if (item.hasOwnProperty(key)) {
                randomValue[key] = item[key];
            }
        }
        return randomValue;
    }

    function getRandomValueText(value) {
        var text = "";
        for (var [key, val] of Object.entries(value)) {
            if (key && val) {
                text += val + "\n";
            }
        }
        return text.trim();
    }

    function resizeTextarea() {
        outputText.style.height = 'auto';
        outputText.style.height = outputText.scrollHeight + 'px';
    }
});
