    <script>
        document.getElementById('dataForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const inputData = document.getElementById('inputData').value;
            fetch('http://localhost:8000', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ value: inputData })
            });
        });
    </script>
