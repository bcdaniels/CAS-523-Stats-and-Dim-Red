# Data for Sosna et al. 2019

**Citation:**<br>
Sosna MMG, Twomey CR, Bak-Coleman J, Poel W, Daniels BC, Romanczuk P, Couzin ID. 2019. [Individual and collective encoding of risk in animal groups](https://www.pnas.org/content/pnas/early/2019/09/17/1905585116.full.pdf). _Proceedings of the National Academy of Sciences._ 116(41): 20556-20561

## Overview
The datasets provided are in CSV or HDF5 format. The R library `rhdf5` can be used to open .h5 files. For example:

```r
library(rhdf5)
file <- 'cascade_sizes.h5'

# Show contents
h5ls(file)

# Load data
data <- h5read(file, 'mat_srk_1_before')
```

### `cascade_sizes.h5`
This dataset consists of matrices of cascade sizes by treatment:
* `mat_srk_1_after`: after Schreckstoff (1st exposure)
* `mat_srk_1_before`: before Schreckstoff (1st exposure)
* `mat_srk_3_after`: after Schreckstoff (3rd exposure)
* `mat_srk_3_before`: before Schreckstoff (3rd exposure)
* `mat_wtr_after`: after water
* `mat_wtr_before`: before water

Each row corresponds to a trial, with columns corresponding to the number of fish that startled in a cascade. The number of columns is set by the most cascades that occurred in a trial, so trials with fewer cascades will have NaNs for some columns.

### `df_n_cascades_srk_1.csv`
This dataset is similar to `cascade_sizes.h5` but adds trial names and simplifies analysis. The columns include `Trial` for trial name, `N_before` for number of cascades prior to Schreckstoff (1st exposure), `N_after` for number of cascades after Schreckstoff, and `Change` for the difference.

### `df_n_cascades_srk_3.csv`
Same as `df_n_cascades_srk_1.csv`, but for the third exposure to Schreckstoff.

### `df_n_cascades_wtr.csv`
Same as `df_n_cascades_srk_1.csv`, but for exposure to water.

### `first_responders_srk1.csv`
This dataset is used for feature selection, fitting the model of startle probability to an initiator, and constructing startle probability networks. Each row is a fish that was the first to respond to an initiating startle (`Response` = 1), or a fish that did _not_ respond to the initiator (`Response` = 0). Startling fish that were not the first responder are excluded from this dataset. This dataset consists of data from water trials and 1st exposure to Schrecksoff.

The columns consist of:
* `Trial`: trial name
* `Event_raw`: the startle cascade, numbered sequentially from the first cascade in the firs ttrial.
* `Event_trial`: the startle cascade number within a trial
* `Response`: whether the fish startled (`0`) or not (`1`)
* `Resp_Int`: the intensity with which the fish responded. A threshold of 110 was used to binarize response intensities into "startled" vs. "did not startle."
* `Initiator`: the intensity with which the initiator startled
* `Log_Init`: the log (base 10) of initiator intensity
* `When`: before vs. after the stimulus
* `Class`: Schreckstoff (1st exposure) or water
* `Dist_metric`: metric distance between initiator and fish
* `Log_dist_metric`: the log (base 10) of metric distance
* `Dist_topological`: the topological distance, i.e. ranked metric distance. If the initiator was the closest fish to the focal individual, topological distance would be 1.
* `Ang_area`: the angular area subtended by the initiator on the focal fish
* `Rank_area`: the rank of the angular area subtended by the initiator on the focal fish. If the initiator takes up the most area in the focal's vision, rank area is 1.
* `Loom`: the change in angular area of the initiator on the focal fish from the frame prior to the startle through 10 frames after (FPS = 120)
* `Log_loom`: the log (base 10) of loom
* `Ang_pos`: the angle (in radians) between the head of the initiator and the head of the focal. This measures whether the initiator was to the left of the focal, in front of it, behind it, etc.
* `Heading`: the absolute value of the angle of the initiator relative to the focal individual. 0 indicates facing the same direction, pi indicates facing opposite directions. Wraps at 2*pi.

### `first_responders_srk3.csv`
Same as `first_responders_srk1.csv`, but for the third exposure to Schreckstoff.

### `NND_data.h5`
Arrays of nearest-neighbor distances for all fish for all trials. Fields are `schreck_1st`, `schreck_3rd`, and `water_1st`. Data dimensions are trial x fish x frame, with padding for fish and frames. Note that fish identities are **not** constant across frames.

For example, `schreck_1st[1, , 1]` corresponds to the NND vector of all fish at the first frame of the first trial in the first Schreckstoff exposure treatment. `schreck_1st[1, , 2]` consists of the NND vector for all fish in the _second_ frame of that trial. The first element of the first vector is not the same fish as the first element of the second vector.
