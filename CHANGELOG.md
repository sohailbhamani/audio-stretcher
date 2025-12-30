# CHANGELOG



## v0.0.0 (2025-12-30)

### Chore

* chore(deps): bump github/codeql-action from 3 to 4 (#6)

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3 to 4.
- [Release notes](https://github.com/github/codeql-action/releases)
- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
- [Commits](https://github.com/github/codeql-action/compare/v3...v4)

---
updated-dependencies:
- dependency-name: github/codeql-action
  dependency-version: &#39;4&#39;
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`f9c50f3`](https://github.com/sohailbhamani/audio-stretcher/commit/f9c50f3b980f062236e89568cfc53bf046c2bb2e))

* chore(deps): bump actions/checkout from 4 to 6 (#5)

Bumps [actions/checkout](https://github.com/actions/checkout) from 4 to 6.
- [Release notes](https://github.com/actions/checkout/releases)
- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
- [Commits](https://github.com/actions/checkout/compare/v4...v6)

---
updated-dependencies:
- dependency-name: actions/checkout
  dependency-version: &#39;6&#39;
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`921a5cd`](https://github.com/sohailbhamani/audio-stretcher/commit/921a5cd2c4ee20f7411d1819a2b8767498fef2c6))

* chore(deps): bump actions/setup-python from 5 to 6 (#4)

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5 to 6.
- [Release notes](https://github.com/actions/setup-python/releases)
- [Commits](https://github.com/actions/setup-python/compare/v5...v6)

---
updated-dependencies:
- dependency-name: actions/setup-python
  dependency-version: &#39;6&#39;
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`1fca3c7`](https://github.com/sohailbhamani/audio-stretcher/commit/1fca3c7b87ed00287114f6905e4ffecd003099da))

* chore(deps): bump codecov/codecov-action from 4 to 5 (#3)

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 4 to 5.
- [Release notes](https://github.com/codecov/codecov-action/releases)
- [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
- [Commits](https://github.com/codecov/codecov-action/compare/v4...v5)

---
updated-dependencies:
- dependency-name: codecov/codecov-action
  dependency-version: &#39;5&#39;
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`29f6d33`](https://github.com/sohailbhamani/audio-stretcher/commit/29f6d33b0d0493f4e49378d86e04500552eaf9d5))

* chore: add CI, Dependabot, Codecov, ruff/mypy config, professional README (#2)

* feat: implement stretch command, tests, and gitignore

* chore: add CI, Dependabot, Codecov, ruff/mypy config, professional README

* style: fix import sorting (ruff I001)

* ci: add security scanning (CodeQL + Trivy)

---------

Co-authored-by: Sohail &lt;sohail@waxlogic.io&gt; ([`06ab18e`](https://github.com/sohailbhamani/audio-stretcher/commit/06ab18ebdba75f3123c46b6a60786fd6dd454e20))

* chore: add OSS files (README, CONTRIBUTING, CODE_OF_CONDUCT, templates) ([`deb7407`](https://github.com/sohailbhamani/audio-stretcher/commit/deb74070403b299ec1f2cd5222e335fd14bb61b1))

### Ci

* ci: add permissions to trivy job for SARIF upload ([`04c3720`](https://github.com/sohailbhamani/audio-stretcher/commit/04c3720721173772b4e322f6ea41f12f95f113e8))

* ci: add CODECOV_TOKEN to codecov-action ([`d25fdce`](https://github.com/sohailbhamani/audio-stretcher/commit/d25fdce98c0abff57397b266c8692493a228a022))

### Test

* test: add stretcher tests (#7)

* test: add time stretching accuracy tests

* fix(test): remove unused import

* chore(release): integrate semantic-release configuration

* refactor(test): move fixtures to conftest.py and organize imports

* fix(test): remove redundant code and organize imports

* fix(test): restore tempfile import and organize

* fix(test): organize imports with from soundfile import read

* fix(test): standardizes imports in conftest.py

* fix(test): organize imports in test_stretching.py

* fix(test): add missing temp_output_path fixture

---------

Co-authored-by: Sohail &lt;sohail@waxlogic.io&gt; ([`29eb20c`](https://github.com/sohailbhamani/audio-stretcher/commit/29eb20c4a2d137eda28d6dff7d87c3994c0ccb8a))

### Unknown

* Initial commit ([`40e6e39`](https://github.com/sohailbhamani/audio-stretcher/commit/40e6e39f4413ac9f0ce6604339fe6b3e36061f0e))
