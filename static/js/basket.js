window.onload = function () {
    $('.basket-list').on('change', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                $('.basket-list').html(data.result);
            },
        });

        event.preventDefault();
    });
}