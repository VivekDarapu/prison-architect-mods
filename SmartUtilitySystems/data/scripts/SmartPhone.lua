local timeTot = 0

function Create()
  timeTot = 90
end

function Update(timePassed)
  timeTot = timeTot + timePassed
  if timeTot >= 60 then
    timeTot = 0
    RunPhoneLogic()
  end
end

function RunPhoneLogic()
  local booths = World.GetNearbyObjects('PhoneBooth', 9999)
  local taps = World.GetNearbyObjects('PhoneTap', 9999)
  
  if not taps or #taps == 0 then
    return
  end
  
  for i, booth in pairs(booths) do
    local isConnected = false
    local conns = booth.GetConnections()
    
    if conns then
      for k, v in pairs(conns) do
        if v.Type == "PhoneTap" then
          isConnected = true
          break
        end
      end
    end
    
    if not isConnected then
      for j, tap in pairs(taps) do
        local tapConns = tap.GetConnections()
        local wiredCount = 0
        
        if tapConns then
          for k, v in pairs(tapConns) do
            if v.Type == "PhoneBooth" then
              wiredCount = wiredCount + 1
            end
          end
        end
        
        if wiredCount == 0 then
          Object.Connect(booth, tap)
          break
        end
      end
    end
  end
end
