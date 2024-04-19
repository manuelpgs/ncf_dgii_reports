#!/usr/bin/env python2.7

SFSDEPT = 50

ESCALA_SALARIAL01 = 34685.00
SFS = 20
AFP = 30

# if 'SFSDEPT' in locals() or 'SFSDEPT' in globals():
#    DEDUCCIONES = SFS + AFP + SFSDEPT
# else:
#    DEDUCCIONES = SFS + AFP

DEDUCCIONES = SFS + AFP + SFSDEPT if 'SFSDEPT' in locals() or 'SFSDEPT' in globals() else SFS + AFP


print DEDUCCIONES


                '''
                    payment.amount could be the amount paid for many invoices
                '''
                invoices_paid = payment._get_invoices() #back01
                # _logger.warning("INVOICES: %s , INVOICE TYPE: %s , INVOICE NUMBER: %s in method get_late_paid_invoice_with_retentions" % (invoice.id, invoice.type, invoice.number))
                # _logger.warning("INVOICES PAID Len: %s" % (len(invoices_paid)))

                for invoice in invoices_paid:                    

                    if payment.journal_id.payment_form == 'cash':
                        commun_data['MONTOS_PAGADOS_EFECTIVO'] += invoice.amount_total_signed
                    elif payment.journal_id.payment_form == 'bank':
                        commun_data['MONTOS_PAGADOS_BANCO'] += invoice.amount_total_signed
                    elif payment.journal_id.payment_form == 'card':
                        commun_data['MONTOS_PAGADOS_TARJETAS'] += invoice.amount_total_signed
                    elif payment.journal_id.payment_form == 'credit': # just in case they have a journal of credit
                        commun_data['MONTOS_A_CREDITO'] += invoice.amount_total_signed
                    elif payment.journal_id.payment_form == 'bond':
                        commun_data['MONTOS_EN_BONOS_O_CERTIFICADOS_REGALOS'] += invoice.amount_total_signed
                    elif payment.journal_id.payment_form == 'swap':
                        commun_data['MONTOS_EN_PERMUTA']  += invoice.amount_total_signed
                    else:
                        commun_data['MONTOS_EN_OTRAS_FORMAS_VENTAS'] += invoice.amount_total_signed # like Bitcoin and others