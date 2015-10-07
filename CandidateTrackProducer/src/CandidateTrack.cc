#include "DataFormats/Math/interface/deltaR.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

CandidateTrack::CandidateTrack () :
  caloEMDRp3_               (numeric_limits<int>::min  ()),
  caloHadDRp3_              (numeric_limits<int>::min  ()),
  caloEMDRp5_               (numeric_limits<int>::min  ()),
  caloHadDRp5_              (numeric_limits<int>::min  ()),
  deltaRToClosestElectron_  (numeric_limits<int>::min  ()),
  deltaRToClosestMuon_      (numeric_limits<int>::min  ()),
  deltaRToClosestTau_       (numeric_limits<int>::min  ()),
  trackIsoDRp3_             (numeric_limits<int>::min  ()),
  trackIsoDRp5_             (numeric_limits<int>::min  ()),
  trackIsoNoPUDRp3_         (numeric_limits<int>::min  ()),
  trackIsoNoPUDRp5_         (numeric_limits<int>::min  ())
{
}

CandidateTrack::CandidateTrack (const reco::Track &track) :
  reco::Track (track),
  caloEMDRp3_               (numeric_limits<int>::min  ()),
  caloHadDRp3_              (numeric_limits<int>::min  ()),
  caloEMDRp5_               (numeric_limits<int>::min  ()),
  caloHadDRp5_              (numeric_limits<int>::min  ()),
  deltaRToClosestElectron_  (numeric_limits<int>::min  ()),
  deltaRToClosestMuon_      (numeric_limits<int>::min  ()),
  deltaRToClosestTau_       (numeric_limits<int>::min  ()),
  trackIsoDRp3_             (numeric_limits<int>::min  ()),
  trackIsoDRp5_             (numeric_limits<int>::min  ()),
  trackIsoNoPUDRp3_         (numeric_limits<int>::min  ()),
  trackIsoNoPUDRp5_         (numeric_limits<int>::min  ())
{
}

CandidateTrack::CandidateTrack (const reco::Track &track, const vector<reco::Track> &tracks, const vector<pat::Electron> &electrons, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus) :
  reco::Track (track),
  caloEMDRp3_              (numeric_limits<int>::min ()),
  caloHadDRp3_             (numeric_limits<int>::min ()),
  caloEMDRp5_              (numeric_limits<int>::min ()),
  caloHadDRp5_             (numeric_limits<int>::min ()),
  deltaRToClosestElectron_ (getMinDeltaR (electrons)),
  deltaRToClosestMuon_     (getMinDeltaR (muons)),
  deltaRToClosestTau_      (getMinDeltaR (taus)),
  trackIsoDRp3_            (getTrackIsolation (track, tracks, false, 0.3)),
  trackIsoDRp5_            (getTrackIsolation (track, tracks, false, 0.5)),
  trackIsoNoPUDRp3_        (getTrackIsolation (track, tracks, true, 0.3)),
  trackIsoNoPUDRp5_        (getTrackIsolation (track, tracks, true, 0.5))
{
}

CandidateTrack::~CandidateTrack ()
{
}

template<class T> const double
CandidateTrack::getMinDeltaR (const vector<T> &objects) const
{
  double minDeltaR = numeric_limits<int>::min ();

  for (const auto &object : objects)
    {
      double dR = deltaR (*this, object);

      if (dR < minDeltaR || minDeltaR < 0.0)
        minDeltaR = dR;
    }

  return minDeltaR;
}

const int
CandidateTrack::missingInnerHits () const
{
  return this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS);
}

const int
CandidateTrack::missingMiddleHits () const
{
  return this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS);
}

const int
CandidateTrack::missingOuterHits () const
{
  return this->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS);
}

const double
CandidateTrack::caloEMDRp3 () const
{
  return this->caloEMDRp3_;
}

const double
CandidateTrack::caloHadDRp3 () const
{
  return this->caloHadDRp3_;
}

const double
CandidateTrack::caloTotDRp3 () const
{
  return this->caloEMDRp3_ + this->caloHadDRp3_;
}

const double
CandidateTrack::caloEMDRp5 () const
{
  return this->caloEMDRp5_;
}

const double
CandidateTrack::caloHadDRp5 () const
{
  return this->caloHadDRp5_;
}

const double
CandidateTrack::caloTotDRp5 () const
{
  return this->caloEMDRp5_ + this->caloHadDRp5_;
}

const double
CandidateTrack::deltaRToClosestElectron () const
{
  return this->deltaRToClosestElectron_;
}

const double
CandidateTrack::deltaRToClosestMuon () const
{
  return this->deltaRToClosestMuon_;
}

const double
CandidateTrack::deltaRToClosestTau () const
{
  return this->deltaRToClosestTau_;
}

const double
CandidateTrack::trackIsoDRp3 () const
{
  return this->trackIsoDRp3_;
}

const double
CandidateTrack::trackIsoDRp5 () const
{
  return this->trackIsoDRp5_;
}

const double
CandidateTrack::trackIsoNoPUDRp3 () const
{
  return this->trackIsoNoPUDRp3_;
}

const double
CandidateTrack::trackIsoNoPUDRp5 () const
{
  return this->trackIsoNoPUDRp5_;
}

const double
CandidateTrack::getTrackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const bool noPU, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      if (noPU && track.dz (t.vertex ()) > 5.0 * hypot (track.dzError (), t.dzError ()))
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}
