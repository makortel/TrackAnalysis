Primary vertex resolution measurement with vertex splitting method
==================================================================

Measurement is split in two parts
* vertex splitting done in CMSSW, produces ntuple with the information of original and split vertices
* analysis of the ntuple: filling histograms, fitting gaussians to the histograms, and making final plots

Recipe for ntuples
------------------

```
cmsrel CMSSW_8_0_<X>
cd CMSSW_8_0_<X>/src
git clone https://github.com/makortel/TrackAnalysis.git
scram b
cd TrackAnalysis/VertexPerformance/test
# edit config.py (*)
cmsRun config.py
```
(*) uncomment e.g. these two lines
[test/config.py#L118](test/config.py#L118)
or add your preferred files

The job produces histograms.root file with the ntuple
(`vertexPerformanceNtuple/tree`). The relevant branches are of type
`std::vector<float>` (even if that is an overkill for this case where
we operate on a single vertex per event).

Here is also the exact crab configuration I have used in the past
[test/crabmulti.py](test/crabmulti.py)


Recipe for ntuple analysis
--------------------------

Here is what to do in the ntuple analysis as a pseudocode (variable names refer to the ntuple branches)
```
# ensure there are vertices
if(pv_fake.empty()) continue;

# require that the PV is good
if(pv_fake[0] || pv_ndof[0] <= 4) continue;

# fill difference histograms
# showing here only a 1D for x, but should be straightforward to extend to y and z, and to arbitrary 2D
h_diff_x->Fill(res_vertex1_x[0] - res_vertex2_x[0])
...

# fill pull histograms
h_pull_x->Fill( (res_vertex1_x[0] - res_vertex2_x[0])/sqrt(res_vertex1_x_error[0]**2 + res_vertex2_x_error[0]**2)
...
```

### Post-processing
- resolution
  * fit gaussian to (the core of) h_diff_x
  * take the gaussian sigma/sqrt(2) as the resolution (multiply with 10000 for cm->um)
- pull
  * fit gaussian to (the core of) h_pull_x
  * take the gaussian sigma as the pull
