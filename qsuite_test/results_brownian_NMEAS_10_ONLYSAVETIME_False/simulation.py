from example.brownian_motion import BrownianMotion

def simulation_code(kwargs):

   bm = BrownianMotion(**kwargs)
   bm.simulate()
   result = bm.get_trajectories()

   return result