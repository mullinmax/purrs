document.addEventListener('DOMContentLoaded', function() {
    // Add feed
    document.getElementById('create-feed-form').addEventListener('submit', function(e) {
        e.preventDefault();
        let url = document.getElementById('new-url').value;
    
        let data = {
            url: url
        };
    
        fetch('/feeds', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Update feed
    let updateForms = document.getElementsByClassName('update-feed-form');
    for (let form of updateForms) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            let id = this.getAttribute('data-id');
            let url = document.getElementById('url-' + id).value;
            fetch('/feeds/' + id, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({url: url}),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                location.reload();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    }

    // Delete feed
    let deleteForms = document.getElementsByClassName('delete-feed-form');
    for (let form of deleteForms) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            let id = this.getAttribute('data-id');
            fetch('/feeds/' + id, {
                method: 'DELETE',
            })
            .then(response => {
                console.log('Success:', response);
                location.reload();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    }
});
