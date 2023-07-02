document.addEventListener('DOMContentLoaded', function() {
    // Function to check if cron expression is valid
    function isValidCronExpression(expression) {
        const regex = /^(((\d+,)+\d+|(\d+(\/|-)\d+)|\d+|\*) ?){5,7}$/;
        return regex.test(expression);
    }

    // Add feed
    document.getElementById('create-feed-form').addEventListener('submit', function(e) {
        e.preventDefault();
        let url = document.getElementById('new-url').value;
        let cronExpression = document.getElementById('cron-expression').value;

        if (!isValidCronExpression(cronExpression)) {
            alert('Invalid cron expression');
            return;
        }

        let data = {
            url: url,
            cron_expression: cronExpression
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
            let cronExpression = document.getElementById('cron-' + id).value;

            if (!isValidCronExpression(cronExpression)) {
                alert('Invalid cron expression');
                return;
            }

            fetch('/feeds/' + id, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({url: url, cron_expression: cronExpression}),
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
