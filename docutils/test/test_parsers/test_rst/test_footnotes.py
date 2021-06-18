#! /usr/bin/env python

# $Id$
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for states.py.
"""
from __future__ import absolute_import

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport


def suite():
    s = DocutilsTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['footnotes'] = [
["""\
.. [1] This is a footnote.
""",
"""\
<document source="test data">
    <footnote ids="footnote-1" names="1">
        <label>
            1
        <paragraph>
            This is a footnote.
"""],
["""\
.. [1] This is a footnote
   on multiple lines.
""",
"""\
<document source="test data">
    <footnote ids="footnote-1" names="1">
        <label>
            1
        <paragraph>
            This is a footnote
            on multiple lines.
"""],
["""\
.. [1] This is a footnote
     on multiple lines with more space.

.. [2] This is a footnote
  on multiple lines with less space.
""",
"""\
<document source="test data">
    <footnote ids="footnote-1" names="1">
        <label>
            1
        <paragraph>
            This is a footnote
            on multiple lines with more space.
    <footnote ids="footnote-2" names="2">
        <label>
            2
        <paragraph>
            This is a footnote
            on multiple lines with less space.
"""],
["""\
.. [1]
   This is a footnote on multiple lines
   whose block starts on line 2.
""",
"""\
<document source="test data">
    <footnote ids="footnote-1" names="1">
        <label>
            1
        <paragraph>
            This is a footnote on multiple lines
            whose block starts on line 2.
"""],
["""\
.. [1]

That was an empty footnote.
""",
"""\
<document source="test data">
    <footnote ids="footnote-1" names="1">
        <label>
            1
    <paragraph>
        That was an empty footnote.
"""],
["""\
.. [1]
No blank line.
""",
"""\
<document source="test data">
    <footnote ids="footnote-1" names="1">
        <label>
            1
    <system_message level="2" line="2" source="test data" type="WARNING">
        <paragraph>
            Explicit markup ends without a blank line; unexpected unindent.
    <paragraph>
        No blank line.
"""],
]

totest['auto_numbered_footnotes'] = [
["""\
[#]_ is the first auto-numbered footnote reference.
[#]_ is the second auto-numbered footnote reference.

.. [#] Auto-numbered footnote 1.
.. [#] Auto-numbered footnote 2.
.. [#] Auto-numbered footnote 3.

[#]_ is the third auto-numbered footnote reference.
""",
"""\
<document source="test data">
    <paragraph>
        <footnote_reference auto="1" ids="footnote-reference-1">
         is the first auto-numbered footnote reference.
        <footnote_reference auto="1" ids="footnote-reference-2">
         is the second auto-numbered footnote reference.
    <footnote auto="1" ids="footnote-1">
        <paragraph>
            Auto-numbered footnote 1.
    <footnote auto="1" ids="footnote-2">
        <paragraph>
            Auto-numbered footnote 2.
    <footnote auto="1" ids="footnote-3">
        <paragraph>
            Auto-numbered footnote 3.
    <paragraph>
        <footnote_reference auto="1" ids="footnote-reference-3">
         is the third auto-numbered footnote reference.
"""],
["""\
[#third]_ is a reference to the third auto-numbered footnote.

.. [#first] First auto-numbered footnote.
.. [#second] Second auto-numbered footnote.
.. [#third] Third auto-numbered footnote.

[#second]_ is a reference to the second auto-numbered footnote.
[#first]_ is a reference to the first auto-numbered footnote.
[#third]_ is another reference to the third auto-numbered footnote.

Here are some internal cross-references to the targets generated by
the footnotes: first_, second_, third_.
""",
"""\
<document source="test data">
    <paragraph>
        <footnote_reference auto="1" ids="footnote-reference-1" refname="third">
         is a reference to the third auto-numbered footnote.
    <footnote auto="1" ids="first" names="first">
        <paragraph>
            First auto-numbered footnote.
    <footnote auto="1" ids="second" names="second">
        <paragraph>
            Second auto-numbered footnote.
    <footnote auto="1" ids="third" names="third">
        <paragraph>
            Third auto-numbered footnote.
    <paragraph>
        <footnote_reference auto="1" ids="footnote-reference-2" refname="second">
         is a reference to the second auto-numbered footnote.
        <footnote_reference auto="1" ids="footnote-reference-3" refname="first">
         is a reference to the first auto-numbered footnote.
        <footnote_reference auto="1" ids="footnote-reference-4" refname="third">
         is another reference to the third auto-numbered footnote.
    <paragraph>
        Here are some internal cross-references to the targets generated by
        the footnotes: \n\
        <reference name="first" refname="first">
            first
        , \n\
        <reference name="second" refname="second">
            second
        , \n\
        <reference name="third" refname="third">
            third
        .
"""],
["""\
Mixed anonymous and labelled auto-numbered footnotes:

[#four]_ should be 4, [#]_ should be 1,
[#]_ should be 3, [#]_ is one too many,
[#two]_ should be 2, and [#six]_ doesn't exist.

.. [#] Auto-numbered footnote 1.
.. [#two] Auto-numbered footnote 2.
.. [#] Auto-numbered footnote 3.
.. [#four] Auto-numbered footnote 4.
.. [#five] Auto-numbered footnote 5.
.. [#five] Auto-numbered footnote 5 again (duplicate).
""",
"""\
<document source="test data">
    <paragraph>
        Mixed anonymous and labelled auto-numbered footnotes:
    <paragraph>
        <footnote_reference auto="1" ids="footnote-reference-1" refname="four">
         should be 4, \n\
        <footnote_reference auto="1" ids="footnote-reference-2">
         should be 1,
        <footnote_reference auto="1" ids="footnote-reference-3">
         should be 3, \n\
        <footnote_reference auto="1" ids="footnote-reference-4">
         is one too many,
        <footnote_reference auto="1" ids="footnote-reference-5" refname="two">
         should be 2, and \n\
        <footnote_reference auto="1" ids="footnote-reference-6" refname="six">
         doesn't exist.
    <footnote auto="1" ids="footnote-1">
        <paragraph>
            Auto-numbered footnote 1.
    <footnote auto="1" ids="two" names="two">
        <paragraph>
            Auto-numbered footnote 2.
    <footnote auto="1" ids="footnote-2">
        <paragraph>
            Auto-numbered footnote 3.
    <footnote auto="1" ids="four" names="four">
        <paragraph>
            Auto-numbered footnote 4.
    <footnote auto="1" dupnames="five" ids="five">
        <paragraph>
            Auto-numbered footnote 5.
    <footnote auto="1" dupnames="five" ids="five-1">
        <system_message backrefs="five-1" level="2" line="12" source="test data" type="WARNING">
            <paragraph>
                Duplicate explicit target name: "five".
        <paragraph>
            Auto-numbered footnote 5 again (duplicate).
"""],
["""\
Mixed manually-numbered, anonymous auto-numbered,
and labelled auto-numbered footnotes:

[#four]_ should be 4, [#]_ should be 2,
[1]_ is 1, [3]_ is 3,
[#]_ should be 6, [#]_ is one too many,
[#five]_ should be 5, and [#six]_ doesn't exist.

.. [1] Manually-numbered footnote 1.
.. [#] Auto-numbered footnote 2.
.. [#four] Auto-numbered footnote 4.
.. [3] Manually-numbered footnote 3
.. [#five] Auto-numbered footnote 5.
.. [#five] Auto-numbered footnote 5 again (duplicate).
.. [#] Auto-numbered footnote 6.
""",
"""\
<document source="test data">
    <paragraph>
        Mixed manually-numbered, anonymous auto-numbered,
        and labelled auto-numbered footnotes:
    <paragraph>
        <footnote_reference auto="1" ids="footnote-reference-1" refname="four">
         should be 4, \n\
        <footnote_reference auto="1" ids="footnote-reference-2">
         should be 2,
        <footnote_reference ids="footnote-reference-3" refname="1">
            1
         is 1, \n\
        <footnote_reference ids="footnote-reference-4" refname="3">
            3
         is 3,
        <footnote_reference auto="1" ids="footnote-reference-5">
         should be 6, \n\
        <footnote_reference auto="1" ids="footnote-reference-6">
         is one too many,
        <footnote_reference auto="1" ids="footnote-reference-7" refname="five">
         should be 5, and \n\
        <footnote_reference auto="1" ids="footnote-reference-8" refname="six">
         doesn't exist.
    <footnote ids="footnote-1" names="1">
        <label>
            1
        <paragraph>
            Manually-numbered footnote 1.
    <footnote auto="1" ids="footnote-2">
        <paragraph>
            Auto-numbered footnote 2.
    <footnote auto="1" ids="four" names="four">
        <paragraph>
            Auto-numbered footnote 4.
    <footnote ids="footnote-3" names="3">
        <label>
            3
        <paragraph>
            Manually-numbered footnote 3
    <footnote auto="1" dupnames="five" ids="five">
        <paragraph>
            Auto-numbered footnote 5.
    <footnote auto="1" dupnames="five" ids="five-1">
        <system_message backrefs="five-1" level="2" line="14" source="test data" type="WARNING">
            <paragraph>
                Duplicate explicit target name: "five".
        <paragraph>
            Auto-numbered footnote 5 again (duplicate).
    <footnote auto="1" ids="footnote-4">
        <paragraph>
            Auto-numbered footnote 6.
"""],
]

totest['auto_symbol_footnotes'] = [
["""\
.. [*] This is an auto-symbol footnote.
""",
"""\
<document source="test data">
    <footnote auto="*" ids="footnote-1">
        <paragraph>
            This is an auto-symbol footnote.
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
