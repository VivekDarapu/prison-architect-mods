local timeTot = 0

function Create()
  timeTot = 90
end

function Update(timePassed)
  timeTot = timeTot + timePassed
  if timeTot >= 60 then
    timeTot = 0
    RunMatrixLogic()
  end
end

function RunMatrixLogic()
  local myCams = World.GetNearbyObjects('Cctv', 9999)
  local myMons = World.GetNearbyObjects('CctvMonitor', 9999)
  
  if not myMons or #myMons == 0 then
    return
  end
  
  local currentMonIdx = 1
  
  for i, cam in pairs(myCams) do
    local isConnected = false
    local conns = cam.GetConnections()
    
    if conns then
      for k, v in pairs(conns) do
        if v.Type == "CctvMonitor" then
          isConnected = true
          break
        end
      end
    end
    
    if not isConnected then
      while currentMonIdx <= #myMons do
        local target = myMons[currentMonIdx]
        local targetConns = target.GetConnections()
        local count = 0
        
        if targetConns then
          for k, v in pairs(targetConns) do
            if v.Type == "Cctv" then
              count = count + 1
            end
          end
        end
        
        if count < 8 then
          Object.Connect(cam, target)
          break
        else
          currentMonIdx = currentMonIdx + 1
        end
      end
    end
  end
end
