# sentinel-findings.md

*Written by Sentinel — WARN-tier findings.*

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.646172+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.646172+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.646172+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.646172+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.646172+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:16141`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.646172+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:22976`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.646172+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:41.821190+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8386`
- **Detail:** `parseInt(t?.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8389`
- **Detail:** `parseInt(t?.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9670`
- **Detail:** `parseInt(diff?.originalCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9673`
- **Detail:** `parseInt(diff?.currentCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9676`
- **Detail:** `parseInt(diff?.addedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9679`
- **Detail:** `parseInt(diff?.removedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9691`
- **Detail:** `parseFloat(diff?.bestSimilarity ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9877`
- **Detail:** `parseInt(rawTrial?.versionCount ?? changes.length, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10015`
- **Detail:** `parseInt(rawTrial?.current?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10042`
- **Detail:** `parseInt(rawTrial?.original?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10057`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.outcomes, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10060`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.primaryOutcomes, 10) ` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10063`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.secondaryOutcomes, 10` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10066`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.enrollmentInfo, 10) |` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10072`
- **Detail:** `parseInt(rawTrial?.outcomesUpdateCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10096`
- **Detail:** `parseInt(rawPack?.summary?.errorCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10528`
- **Detail:** `parseInt(entry?.ctgov ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10531`
- **Detail:** `parseInt(entry?.pubmed ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10534`
- **Detail:** `parseInt(entry?.openalex ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43883`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43927`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43989`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:58:44.394711+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.471390+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.471390+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.471390+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.471390+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.471390+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:16141`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.471390+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:22976`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.471390+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:58:57.644215+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8386`
- **Detail:** `parseInt(t?.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8389`
- **Detail:** `parseInt(t?.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9670`
- **Detail:** `parseInt(diff?.originalCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9673`
- **Detail:** `parseInt(diff?.currentCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9676`
- **Detail:** `parseInt(diff?.addedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9679`
- **Detail:** `parseInt(diff?.removedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9691`
- **Detail:** `parseFloat(diff?.bestSimilarity ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9877`
- **Detail:** `parseInt(rawTrial?.versionCount ?? changes.length, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10015`
- **Detail:** `parseInt(rawTrial?.current?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10042`
- **Detail:** `parseInt(rawTrial?.original?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10057`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.outcomes, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10060`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.primaryOutcomes, 10) ` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10063`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.secondaryOutcomes, 10` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10066`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.enrollmentInfo, 10) |` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10072`
- **Detail:** `parseInt(rawTrial?.outcomesUpdateCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10096`
- **Detail:** `parseInt(rawPack?.summary?.errorCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10528`
- **Detail:** `parseInt(entry?.ctgov ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10531`
- **Detail:** `parseInt(entry?.pubmed ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10534`
- **Detail:** `parseInt(entry?.openalex ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43883`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43927`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43989`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:00.192250+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:17.870698+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:17.870698+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:17.870698+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:17.870698+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:17.870698+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:16141`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:17.870698+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:22976`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:17.870698+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:18.177122+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8386`
- **Detail:** `parseInt(t?.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8389`
- **Detail:** `parseInt(t?.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9670`
- **Detail:** `parseInt(diff?.originalCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9673`
- **Detail:** `parseInt(diff?.currentCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9676`
- **Detail:** `parseInt(diff?.addedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9679`
- **Detail:** `parseInt(diff?.removedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9691`
- **Detail:** `parseFloat(diff?.bestSimilarity ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9877`
- **Detail:** `parseInt(rawTrial?.versionCount ?? changes.length, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10015`
- **Detail:** `parseInt(rawTrial?.current?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10042`
- **Detail:** `parseInt(rawTrial?.original?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10057`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.outcomes, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10060`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.primaryOutcomes, 10) ` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10063`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.secondaryOutcomes, 10` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10066`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.enrollmentInfo, 10) |` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10072`
- **Detail:** `parseInt(rawTrial?.outcomesUpdateCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10096`
- **Detail:** `parseInt(rawPack?.summary?.errorCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10528`
- **Detail:** `parseInt(entry?.ctgov ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10531`
- **Detail:** `parseInt(entry?.pubmed ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10534`
- **Detail:** `parseInt(entry?.openalex ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43883`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43927`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43989`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:21.224107+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.632225+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.632225+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.632225+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.632225+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.632225+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:16141`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.632225+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:22976`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.632225+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T11:59:30.829752+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8386`
- **Detail:** `parseInt(t?.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8389`
- **Detail:** `parseInt(t?.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9670`
- **Detail:** `parseInt(diff?.originalCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9673`
- **Detail:** `parseInt(diff?.currentCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9676`
- **Detail:** `parseInt(diff?.addedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9679`
- **Detail:** `parseInt(diff?.removedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9691`
- **Detail:** `parseFloat(diff?.bestSimilarity ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9877`
- **Detail:** `parseInt(rawTrial?.versionCount ?? changes.length, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10015`
- **Detail:** `parseInt(rawTrial?.current?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10042`
- **Detail:** `parseInt(rawTrial?.original?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10057`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.outcomes, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10060`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.primaryOutcomes, 10) ` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10063`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.secondaryOutcomes, 10` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10066`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.enrollmentInfo, 10) |` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10072`
- **Detail:** `parseInt(rawTrial?.outcomesUpdateCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10096`
- **Detail:** `parseInt(rawPack?.summary?.errorCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10528`
- **Detail:** `parseInt(entry?.ctgov ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10531`
- **Detail:** `parseInt(entry?.pubmed ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10534`
- **Detail:** `parseInt(entry?.openalex ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43883`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43927`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43989`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T11:59:33.504355+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:40`
- **Detail:** pattern matched: pat = re.compile(r"\{\{[^}]+\}\}|REPLACE_ME|__PLACEHOLDER__|TODO_FILL")
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:02:39.742984+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.455336+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.455336+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.455336+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.455336+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.455336+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:16141`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.455336+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:22976`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.455336+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:40.611492+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8386`
- **Detail:** `parseInt(t?.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8389`
- **Detail:** `parseInt(t?.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9670`
- **Detail:** `parseInt(diff?.originalCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9673`
- **Detail:** `parseInt(diff?.currentCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9676`
- **Detail:** `parseInt(diff?.addedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9679`
- **Detail:** `parseInt(diff?.removedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9691`
- **Detail:** `parseFloat(diff?.bestSimilarity ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9877`
- **Detail:** `parseInt(rawTrial?.versionCount ?? changes.length, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10015`
- **Detail:** `parseInt(rawTrial?.current?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10042`
- **Detail:** `parseInt(rawTrial?.original?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10057`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.outcomes, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10060`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.primaryOutcomes, 10) ` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10063`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.secondaryOutcomes, 10` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10066`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.enrollmentInfo, 10) |` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10072`
- **Detail:** `parseInt(rawTrial?.outcomesUpdateCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10096`
- **Detail:** `parseInt(rawPack?.summary?.errorCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10528`
- **Detail:** `parseInt(entry?.ctgov ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10531`
- **Detail:** `parseInt(entry?.pubmed ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10534`
- **Detail:** `parseInt(entry?.openalex ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43883`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43927`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43989`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:42.610727+00:00

## [WARN] P1-unpopulated-placeholder
- **Location:** `test_smoke.py:40`
- **Detail:** pattern matched: pat = re.compile(r"\{\{[^}]+\}\}|REPLACE_ME|__PLACEHOLDER__|TODO_FILL")
- **Fix hint:** Populate the placeholder or escape it before shipping. If the braces are intentional template syntax in a non-template file, exclude the file path via the rule's exclude list.

- **Source:** html-apps.md#safety-checks
- **When:** 2026-06-13T12:02:51.610480+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.245094+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.245094+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.245094+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.245094+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.245094+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:16141`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.245094+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:22976`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.245094+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:02:52.386163+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8386`
- **Detail:** `parseInt(t?.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8389`
- **Detail:** `parseInt(t?.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9670`
- **Detail:** `parseInt(diff?.originalCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9673`
- **Detail:** `parseInt(diff?.currentCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9676`
- **Detail:** `parseInt(diff?.addedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9679`
- **Detail:** `parseInt(diff?.removedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9691`
- **Detail:** `parseFloat(diff?.bestSimilarity ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9877`
- **Detail:** `parseInt(rawTrial?.versionCount ?? changes.length, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10015`
- **Detail:** `parseInt(rawTrial?.current?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10042`
- **Detail:** `parseInt(rawTrial?.original?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10057`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.outcomes, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10060`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.primaryOutcomes, 10) ` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10063`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.secondaryOutcomes, 10` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10066`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.enrollmentInfo, 10) |` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10072`
- **Detail:** `parseInt(rawTrial?.outcomesUpdateCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10096`
- **Detail:** `parseInt(rawPack?.summary?.errorCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10528`
- **Detail:** `parseInt(entry?.ctgov ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10531`
- **Detail:** `parseInt(entry?.pubmed ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10534`
- **Detail:** `parseInt(entry?.openalex ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43883`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43927`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43989`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:02:54.181398+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:2364`
- **Detail:** NCT12345678 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT12345678 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.547131+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5080`
- **Detail:** NCT01035255 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01035255 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.547131+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5083`
- **Detail:** NCT01920711 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01920711 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.547131+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5086`
- **Detail:** NCT02924727 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT02924727 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.547131+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:5089`
- **Detail:** NCT03988634 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT03988634 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.547131+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:16141`
- **Detail:** NCT01206062 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT01206062 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.547131+00:00

## [WARN] P1-fabrication-orphan-trial
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:22976`
- **Detail:** NCT05901831 mentioned in body but not in realData — orphan trial reference: either the trial was dropped during extraction (update prose) or the citation is fabricated
- **Fix hint:** verify NCT05901831 against ClinicalTrials.gov; either add it to realData with full extracted fields, or remove the prose citation if it was inherited from a different paper
- **Source:** F:\e156\docs\assurance-standard.md#data-provenance-match  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.547131+00:00

## [WARN] P1-fabrication-round-number-cluster
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:1`
- **Detail:** 4 suspicious round-number categories firing (cohort_round, p_round, or_perfect_null, or_double_round) — possible fabrication tell
- **Fix hint:** verify the quoted values against the source
- **Source:** F:\e156\docs\assurance-standard.md#data-checking  (BadScientist family, arXiv 2510.18003)
- **When:** 2026-06-13T12:03:12.667604+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:7750`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8113`
- **Detail:** `parseInt(t.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8386`
- **Detail:** `parseInt(t?.data?.tN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:8389`
- **Detail:** `parseInt(t?.data?.cN ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9670`
- **Detail:** `parseInt(diff?.originalCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9673`
- **Detail:** `parseInt(diff?.currentCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9676`
- **Detail:** `parseInt(diff?.addedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9679`
- **Detail:** `parseInt(diff?.removedCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9691`
- **Detail:** `parseFloat(diff?.bestSimilarity ??    ) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:9877`
- **Detail:** `parseInt(rawTrial?.versionCount ?? changes.length, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10015`
- **Detail:** `parseInt(rawTrial?.current?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10042`
- **Detail:** `parseInt(rawTrial?.original?.enrollmentInfo?.count, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10057`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.outcomes, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10060`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.primaryOutcomes, 10) ` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10063`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.secondaryOutcomes, 10` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10066`
- **Detail:** `parseInt(rawTrial?.lastUpdateVersions?.enrollmentInfo, 10) |` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10072`
- **Detail:** `parseInt(rawTrial?.outcomesUpdateCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10096`
- **Detail:** `parseInt(rawPack?.summary?.errorCount, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10528`
- **Detail:** `parseInt(entry?.ctgov ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10531`
- **Detail:** `parseInt(entry?.pubmed ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:10534`
- **Detail:** `parseInt(entry?.openalex ?? 0, 10) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43883`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43927`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:43989`
- **Detail:** `parseInt(r.k) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44321`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `ICOSAPENT_ETHYL_REVIEW.html:44339`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(t.data.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:35`
- **Detail:** `Number(rd.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.tE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00

## [WARN] P2-numeric-parse-or-null
- **Location:** `index.html:53`
- **Detail:** `Number(d.cE) || 0` drops 0/0.0 silently — parsed zero is falsy and falls through to the right-hand fallback
- **Fix hint:** use `Number.isFinite(parsed) ? parsed : null` after a single parseFloat/parseInt/Number call
- **Source:** lessons.md#javascript--html  (parseFloat(x) || null drops 0.0)
- **When:** 2026-06-13T12:03:14.347117+00:00
