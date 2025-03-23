using Ansys.ACT.Interfaces.Common;
using Ansys.ACT.Interfaces.Mesh;
using Ansys.ACT.Interfaces.Mechanical;
using Ansys.ACT.Interfaces.UserObject;

namespace CSharp
{
    public class Load
    {
        private readonly IMechanicalExtAPI _api;
        private readonly IMechanicalUserLoad _load;
        public Load(IExtAPI api, IUserLoad load)
        {
            _api = (IMechanicalExtAPI) api;
            _load = (IMechanicalUserLoad) load;
        }
