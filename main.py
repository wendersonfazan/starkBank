import schedule
import time
from user import settingUser
from invoices import invoices
from transfer import transfer

settingUser.SettingUserClass()
getAmountInvoices = invoices.GetAmountInvoices()
transfer = transfer.transferAmount(getAmountInvoices)
schedule.every(3).hours.do(invoices.InvoicesGenerate())

while True:
    schedule.run_pending()
    time.sleep(1)
