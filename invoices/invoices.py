import starkbank
import random
from datetime import datetime


def GetAmountInvoices():
    invoices = starkbank.invoice.query(
        status="paid"
    )

    invoices = list(invoices)
    values = []

    for invoice in invoices:
        amount = invoice.amount
        values.append(amount)

    fullValueInvoice = sum(values)
    return fullValueInvoice


def InvoicesGenerate():
    customers = dict([('Arya Stark', '29.176.331/0001-69'), ('Iron Bank S.A.', '20.018.183/0001-80'),
                      ('Pessoa 3', '767.688.054-87'), ('Pessoa 2', '174.912.783-02'), ('Pessoa 1', '871.160.553-71'),
                      ('Teste python2', '502.941.068-63')])
    namePaying, documentPaying = random.choice(list(customers.items()))
    discounts = random.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    i = 1
    while i <= 12:
        invoices = starkbank.invoice.create([
            starkbank.Invoice(
                amount=random.randint(1, 999999),
                descriptions=[{'key': 'Arya', 'value': 'Not today'}],
                discounts=[{'percentage': discounts, 'due': datetime(2022, 3, 12, 15, 23, 26, 689377)}],
                due=datetime(2022, 5, 12, 15, 23, 26, 689377),
                expiration=123456789,
                fine=2.5,
                interest=1.3,
                name=namePaying,
                tags=['New sword', 'Invoice #1234'],
                tax_id=documentPaying
            )
        ])

        print(invoices)
        i += 1
    exit()
