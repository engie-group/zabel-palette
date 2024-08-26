# zabel-palette

## Overview

**A very rough collection of miscellaneous tools and helpers that are or were used in the
Zabel platform.**

It provides nine modules:

- _zabel.palette.async_
- _zabel.palette.date_
- _zabel.palette.db_
- _zabel.palette.html_
- _zabel.palette.http_
- _zabel.palette.i18n_
- _zabel.palette.misc_
- _zabel.palette.text_
- _zabel.palette.timeline_

The _zabel.palette.db_ makes use of the `psychopg2` package, the other modules have no
external dependencies.

### zabel.palette.html

This module provides a few functions to help with HTML generation.

- `make_action()`  Return HTML-ready representation for action.
- `make_barchart()`  Return HTML-ready representation for barchart.
- `make_block()`  Return HTML-ready block section.
- `make_dialog()`  Return HTML-ready representation for dialog.
- `make_doughnut()`  Return HTML-ready representation for doughnut.
- `make_element()`  Return HTML-ready representation for element.
- `make_js_button()`  Return HTML-ready representation for button with onclick action.
- `make_linechart()`  Return HTML-ready representation for linechart.
- `make_select()`  Return HTML-ready representation for select block.
- `make_table()`  Return HTML-ready tabular representation for source.
- `make_venn5()`  Return HTML-ready representation for a Venn diagram.
- `make_warning()`  "Return HTML-ready representation for warning t.

### zabel.palette.text

- `plural(count, mark='s')`  Return the plural mark ('s' by default) if `count` is not 1.
- `pretty(n)`  Return a locale-pretty form of number `n` or 'n/a' if not a number.
- `small(t)`  Return `t` in a span block with class small.
- `pprint(ls, file=None)`  Write `ls` on file, removing unnecessary spaces for lines in `ls`.
- `safe(s, spaces=None)` Return an HTML-safe version of `s`, optionnaly replacing spaces.

## License

```text
Copyright (c) 2019-2023 Martin Lafaix (martin.lafaix@external.engie.com) and others

This program and the accompanying materials are made
available under the terms of the Eclipse Public License 2.0
which is available at https://www.eclipse.org/legal/epl-2.0/

SPDX-License-Identifier: EPL-2.0
```
