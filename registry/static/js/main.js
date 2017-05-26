$(function() {
    $('#btn_formset_end_points').click(function() {
        var form_idx = $('#id_end_points-TOTAL_FORMS').val();
        $('#formset_end_points').append($('#empty_formset_end_points').html().replace(/__prefix__/g, form_idx));
        $('#id_end_points-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

    $('#btn_formset_documents').click(function() {
        var form_idx = $('#id_documents-TOTAL_FORMS').val();
        $('#formset_documents').append($('#empty_formset_documents').html().replace(/__prefix__/g, form_idx));
        $('#id_documents-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

})
