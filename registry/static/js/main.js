$(function() {
    $('#btn_formset_end_points').click(function() {
        var form_idx = $('#id_end_points-TOTAL_FORMS').val();
        $('#formset_end_points').append($('#empty_formset_end_points').html().replace(/__prefix__/g, form_idx));
        $('#id_end_points-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

    $('#btn_formset_contact_points').click(function() {
        var form_idx = $('#id_contact_points-TOTAL_FORMS').val();
        $('#formset_contact_points').append($('#empty_formset_contact_points').html().replace(/__prefix__/g, form_idx));
        $('#id_contact_points-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

    $('#btn_formset_documents').click(function() {
        var form_idx = $('#id_documents-TOTAL_FORMS').val();
        $('#formset_documents').append($('#empty_formset_documents').html().replace(/__prefix__/g, form_idx));
        $('#id_documents-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

    $('#btn_formset_technical_interface_bindings').click(function() {
        var form_idx = $('#id_technical_interface_bindings-TOTAL_FORMS').val();
        $('#formset_technical_interface_bindings').append($('#empty_formset_technical_interface_bindings').html().replace(/__prefix__/g, form_idx));
        $('#id_technical_interface_bindings-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

    $('#btn_formset_data_exchange_formats').click(function() {
        var form_idx = $('#id_data_exchange_formats-TOTAL_FORMS').val();
        $('#formset_data_exchange_formats').append($('#empty_formset_data_exchange_formats').html().replace(/__prefix__/g, form_idx));
        $('#id_data_exchange_formats-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

})
