import config
from store import DbToMysql

store = DbToMysql(config.EHCO_DB)


def get_invite_code():
    res = store.find_by_fields('shadowsocks_invitecode', {
                               'code_id': 1, 'isused': 0})
    return res[0]['code']



