from rest_framework.generics import ListAPIView
from app.models import Player
from .serializers import PlayerSerializer

class PlayersListAPIView(ListAPIView):

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    fields = ('playerId', 'gamesPlayed', 'players_details_givenName', 'players_details_surname',
    'players_details_heightCm', 'players_details_weightKg', 'players_details_jumperNumber',
    'players_details_kickingFoot', 'players_details_stateOfOrigin', 'players_details_position',
    'players_details_photoURL', 'team_teamName', 'team_teamAbbr', 'team_teamNickname', 'team_teamId',
    'totals_matchesPlayed', 'totals_timeOnGroundPercentage', 'totals_behinds', 'totals_bounces', 'totals_centreClearances',
    'totals_clangers', 'totals_contestDefLosses', 'totals_contestDefLossPercentage', 'totals_contestDefOneOnOnes',
    'totals_contestedMarks', 'totals_contestedPossessionRate', 'totals_contestedPossessions',
    'totals_contestOffOneOnOnes', 'totals_contestOffWins', 'totals_contestOffWinsPercentage',
    'totals_defHalfPressureActs', 'totals_disposalEfficiency', 'totals_disposals', 'totals_dreamTeamPoints',
    'totals_effectiveDisposals', 'totals_effectiveKicks', 'totals_f50GroundBallGets', 'totals_freesAgainst',
    'totals_freesFor', 'totals_goalAccuracy', 'totals_goalAssists', 'totals_goals', 'totals_groundBallGets',
    'totals_handballs', 'totals_hitouts', 'totals_hitoutsToAdvantage', 'totals_hitoutToAdvantageRate',
    'totals_hitoutWinPercentage', 'totals_inside50s', 'totals_interceptMarks', 'totals_intercepts',
    'totals_kickEfficiency', 'totals_kicks', 'totals_kickToHandballRatio', 'totals_marks', 'totals_marksInside50',
    'totals_marksOnLead', 'totals_metresGained', 'totals_onePercenters', 'totals_pressureActs',
    'totals_ranking', 'totals_ratingPoints', 'totals_rebound50s', 'totals_ruckContests', 'totals_scoreInvolvements',
    'totals_scoreLaunches', 'totals_shotsAtGoal', 'totals_spoils', 'totals_stoppageClearances',
    'totals_tackles', 'totals_tacklesInside50', 'totals_totalClearances', 'totals_totalPossessions',
    'totals_turnovers', 'totals_uncontestedPossessions', 'averages_matchesPlayed', 'averages_timeOnGroundPercentage',
    'averages_behinds', 'averages_bounces', 'averages_centreClearances', 'averages_clangers', 'averages_contestDefLosses',
    'averages_contestDefLossPercentage', 'averages_contestDefOneOnOnes', 'averages_contestedMarks', 'averages_contestedPossessionRate',
    'averages_contestedPossessions', 'averages_contestOffOneOnOnes', 'averages_contestOffWins', 'averages_contestOffWinsPercentage',
    'averages_defHalfPressureActs', 'averages_disposalEfficiency', 'averages_disposals', 'averages_dreamTeamPoints', 'averages_effectiveDisposals',
    'averages_effectiveKicks', 'averages_f50GroundBallGets', 'averages_freesAgainst', 'averages_freesFor', 'averages_goalAccuracy', 'averages_goalAssists',
    'averages_goals', 'averages_groundBallGets', 'averages_handballs', 'averages_hitouts', 'averages_hitoutsToAdvantage',
    'averages_hitoutToAdvantageRate', 'averages_hitoutWinPercentage', 'averages_inside50s', 'averages_interceptMarks', 'averages_intercepts',
    'averages_kickEfficiency', 'averages_kicks', 'averages_kickToHandballRatio', 'averages_marks', 'averages_marksInside50', 'averages_marksOnLead',
    'averages_metresGained', 'averages_onePercenters', 'averages_pressureActs', 'averages_ratingPoints', 'averages_rebound50s', 'averages_ruckContests',
    'averages_scoreInvolvements', 'averages_scoreLaunches', 'averages_shotsAtGoal', 'averages_spoils', 'averages_stoppageClearances', 'averages_tackles',
    'averages_tacklesInside50', 'averages_totalClearances', 'averages_totalPossessions', 'averages_turnovers', 'averages_uncontestedPossessions')