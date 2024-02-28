// Purpose: This file contains the functions that are used to submit forms and display alerts.
function submitFormWithAlert(formId, url, type) {
    $(document).ready(function(){
        $(`#${formId}`).submit(function(e){
            e.preventDefault();
            $.ajax({
                url: url,
                type: type,
                data: $(`#${formId}`).serialize(),
                success: function(response){
                    if(response.message) {
                        alert(response.message);
                    }
                },
                error: function(error){
                    if(error.responseJSON.message) {
                        alert(error.responseJSON.message);
                    }
                }
            });
        });
    });
}

submitFormWithAlert("createUserForm", "/create_user", 'post');
submitFormWithAlert("getUserForm", "/get_user", 'post');
submitFormWithAlert("updateUserForm", "/update_user", 'post');
submitFormWithAlert("deleteUserForm", "/delete_user", 'post');