=======
CHANGES
=======

3.0 (2023-02-17)
----------------

- Add support for Python 3.8, 3.9, 3.10, 3.11.

- Drop support for Python 2.7, 3.4, 3.5, 3.6.


2.1 (2018-12-01)
----------------

- Add support for Python 3.5 up to 3.7.

- Drop support for Python 2.6 and 3.3.

- Drop the ability to run the tests using `python setup.py test`.


2.0.0 (2015-11-09)
------------------

- Standardize namespace __init__.

- Claim Python 3.4 support.


2.0.0a1 (2013-03-03)
--------------------

- Added support for Python 3.3.

- Changed ``zope.testbrowser`` tests to ``WebTest``, since ``zope.testbrowser``
  is not yet ported.

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.


1.10.1 (2012-03-03)
-------------------

- Added adapter registration for `zope.browserresource.interfaces.IETag`
  interface to be available on ``IPageletBrowserLayer``. This adapter is
  necessary to deliver file resources.


1.10.0 (2012-02-23)
-------------------

- Sets HTTP status code to 500 on system errors but only in devmode and in
  tests.


1.9.0 (2010-10-13)
------------------

- Re-release of 1.8.1 as the changes in it require a new major release
  because they broke `z3c.authviewlet`.


1.8.2 (2010-10-13)
------------------

- Re-release of 1.8.0 as the changes in 1.8.1 require a new major
  release because they break `z3c.authviewlet`.


1.8.1 (2010-10-11)
------------------

- Doing redirect in ``UnauthorizedPagelet`` now in ``update`` method instead
  of ``render`` so the layout templage does not get rendered when
  redirecting.

- Fixed tests: Using manager account, so anonymous user does not need to get
  all permissions for running tests successfully.

- Got rid of `zope.app.testing` test dependency by using `zope.app.wsgi`.

- Got rid of `zope.app.authentication` test dependency.

- Added a test for ``403 Forbidden``.


1.8.0 (2010-08-20)
------------------

- Requiring `zope.login` so tests run with `zope.publisher` >= 3.12.


1.7.0 (2009-12-24)
------------------

- Added i18n domains to templates, so they can be translated. (Done
  using `z3c.locales`.)


1.6.1 (2009-12-23)
------------------

- Moved `zope.browserresource` from test dependencies to install
  dependencies as it is needed in the ZCML configuration.


1.6.0 (2009-11-30)
------------------

- Changed view for ``zope.publisher.interfaces.ITraversalException`` from
  system error pagelet to not found pagelet.

- Moved authentication viewlets to `z3c.authviewlet`.

- Cleaned up dependencies, reflecting changes in zope packages.

- Cleaned up test dependencies.


1.5.0 (2009-05-28)
------------------

- Removed dependency on ``zope.app.exception`` by using
  ``zope.browser>=1.2`` and by implementing the exception view classes
  directly instead of inheriting them (Quite nothing of the base
  classes was in use here.)

- Removed not necessary test dependency on ``zope.app.twisted``.

- Removed no longer necessary test dependency on ``zope.app.component``.


1.4.0 (2009-03-16)
------------------

- Removed direct dependency on ``zope.app.security`` by using the new
  packages ``zope.authentication`` and ``zope.principalregistry``.

- Removed not needed test-dependency on ``zope.app.zcmlfiles``.

- Fixed namespace package declaration in ``setup.py``.


1.3.0 (2009-03-13)
------------------

- Implemented login and logout using pagelets resp. viewlets.

- Updated tests to use new ``zope.configuration`` which containts the
  exclude directive.


1.2.1 (2009-02-21)
------------------

- Release 1.2.0 was missing the test file for the security issue.


1.2.0 (2009-02-21)
------------------

- **Security issue:** The traverser defined for
  ``IPageletBrowserLayer`` was a trusted adapter, so the security
  proxy got removed from each traversed object. Thus all sub-objects
  were publically accessable, too.


1.1.0 (2009-02-14)
------------------

- Bugfix: use IContentTemplate instead of IPageTemplate which avoids to get the
  layout template if no IPageTemplate is registered.

- Using ``zope.location.interfaces.ISite`` instead of
  ``zope.app.component.interfaces.ISite``.

- Using ``zope.container`` instead of ``zope.app.container``.

- Cleaned up dependencies.


1.0.2 (2009-04-03)
------------------

- backport release, see release date

- **Security issue:** The traverser defined for
  ``IPageletBrowserLayer`` was a trusted adapter, so the security
  proxy got removed from each traversed object. Thus all sub-objects
  were publically accessable, too.

  Making this change might BREAK your application!
  That means if security is not well declared.

- Bugfix: use IContentTemplate instead of IPageTemplate which avoids to get the
  layout template if no IPageTemplate is registered


1.0.1 (2008-01-24)
------------------

- Bug: Update meta data.


1.0.0 (2008-01-21)
------------------

- Restructure: Move ``z3c.layer.pagelet`` package to it's own top level
  package form ``z3c.layer`` to ``z3c.layer.pagelet``.

- Restructure: Removed ``zope.app.form`` support from pagelet layer.


0.2.3 (2007-11-07)
------------------

- Forward-Bug: Due to a bug in mechanize, the testbrowser throws
  ``httperror_seek_wrapper`` instead of ``HTTPError`` errors. Thanks to RE
  normalizers, the code will now work whether the bug is fixed or not in
  mechanize.


0.2.2 (2007-10-31)
------------------

- Bug: Fixed package meta-data.

- Bug: Fixed test failures due to depency updates.

- Restructure: Fixed deprecation warning for ``ZopeSecurityPolicy``.


0.2.1 (2007-??-??)
------------------

- Changes unknown.


0.2.0 (2007-??-??)
------------------

- Initial release.
