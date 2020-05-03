from ocflib.vhost.application import get_app_vhosts
from ocflib.vhost.mail import get_mail_vhosts
from ocflib.vhost.mail import vhosts_for_user
from ocflib.vhost.web import get_vhosts
from ocflib.vhost.web import has_vhost


def test_app_vhosts():
    app_vhosts = get_app_vhosts()

    # Make sure we're actually getting some app vhosts back
    assert(any(app_vhosts))

    # Check that dev-app.o.b.e exists as an app vhost (this is used for testing
    # by OCF staff, so it's likely to stick around). It should also be owned by
    # the ggroup user.
    assert('dev-app.ocf.berkeley.edu' in app_vhosts)
    assert(app_vhosts['dev-app.ocf.berkeley.edu']['username'] == 'ggroup')

    # Ensure that there's no nossl flags present, we only support SSL vhosts
    # as of rt#5347
    nossl_flags = [
        vhost['flags']
        for vhost in app_vhosts.values() if 'nossl' in vhost['flags']
    ]
    assert(not any(nossl_flags))


def test_mail_vhosts():
    mail_vhosts = get_mail_vhosts()

    # Make sure we're actually getting some app vhosts back
    assert(any(mail_vhosts))

    # Check that the ggroup user has some mail vhosts (these are used for
    # testing by OCF staff so they're likely to stick around)
    assert(any(vhosts_for_user('ggroup')))

    # Check that dev-vhost.o.b.e exists as an mail vhost (this is used for
    # testing by OCF staff, so it's likely to stick around)
    assert(
        'dev-vhost.ocf.berkeley.edu' in {vhost.domain for vhost in mail_vhosts}
    )


def test_web_vhosts():
    web_vhosts = get_vhosts()

    # Make sure we're actually getting some vhosts back
    assert(any(web_vhosts))

    # Ensure the 'staff' and 'ggroup' users have some vhosts. These are likely
    # to always stick around as they are owned by the OCF and there are
    # multiple of them present for each user
    assert(has_vhost('staff'))
    assert(has_vhost('ggroup'))

    # Check that dev-vhost.o.b.e exists as a web vhost (this is used for
    # testing by OCF staff, so it's likely to stick around). It should also
    # have a dev-host-alias.o.b.e alias present
    assert('dev-vhost.ocf.berkeley.edu' in web_vhosts)
    aliases = web_vhosts['dev-vhost.ocf.berkeley.edu']['aliases']
    assert('dev-vhost-alias.ocf.berkeley.edu' in aliases)

    flags = [vhost['flags'] for vhost in web_vhosts.values() if vhost['flags']]
    # Ensure that there's no nossl flags present, we only support SSL vhosts
    # as of rt#5347.
    assert(not any([flag_list for flag_list in flags if 'nossl' in flag_list]))
    # hsts flags are still allowed (but may become the default sometime and be
    # removed)
    assert(any([flag_list for flag_list in flags if 'hsts' in flag_list]))
