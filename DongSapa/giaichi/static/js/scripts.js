$(document).ready(function () {
    $('form').submit(function (event) {
        event.preventDefault();
        var formData = new FormData(this)

        $('form').find('input, select, textarea').each(function () {
            var name = $(this).attr('name');
            var value = $(this).val();

            if (value && name !== 'csrfmiddlewaretoken') {
                formData.append(name, value);
            }
        });

        var fileInput = $('input[type="file"]')[0];
        if (fileInput && fileInput.files.length > 0) {
            formData.append('file', fileInput.files[0]);
        }

        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        console.log(formData)
        $.ajax(
            {
                url: '{% url "giaichi_create"%}',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                headers: {
                    'X-CSRFToken': csrfToken
                },
                success: function (response) {
                    if (response.status == 'Success') {
                        alert(response.message)
                    }
                    else {
                        alert('error')
                    }
                },
                error: function () {
                    alert('Error');
                }
            }
        )
    })
})